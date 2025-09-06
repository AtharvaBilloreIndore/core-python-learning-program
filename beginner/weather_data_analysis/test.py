import unittest
from unittest.mock import patch, mock_open
import os
import json

from main import (
    load_weather_data,
    save_weather_data,
    compute_average,
    analyze_weather,
    add_new_weather_entry
)

class TestLoadWeatherData(unittest.TestCase):
    """Tests for the load_weather_data() function."""

    @patch("os.path.exists", return_value=True)
    @patch("os.path.getsize", return_value=50)
    @patch("builtins.open", new_callable=mock_open, read_data='[{"date": "2025-07-01", "temperature": 25, "humidity": 40, "wind_speed": 10, "precipitation": 0}]')
    def test_load_valid_data(self, mock_file, mock_size, mock_exists):
        """Should return list with one valid weather record."""
        result = load_weather_data()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['temperature'], 25)

    @patch("os.path.exists", return_value=True)
    @patch("os.path.getsize", return_value=0)
    def test_load_empty_file(self, mock_size, mock_exists):
        """Should return an empty list when the file is empty."""
        result = load_weather_data()
        self.assertEqual(result, [])

    @patch("os.path.exists", return_value=False)
    def test_file_does_not_exist(self, mock_exists):
        """Should return an empty list when the file does not exist."""
        result = load_weather_data()
        self.assertEqual(result, [])

    @patch("os.path.exists", return_value=True)
    @patch("os.path.getsize", return_value=100)
    @patch("builtins.open", new_callable=mock_open, read_data='INVALID JSON')
    @patch("builtins.print")
    def test_load_corrupted_json(self, mock_print, mock_file, mock_size, mock_exists):
        """Should return an empty list and print error for corrupt JSON."""
        result = load_weather_data()
        self.assertEqual(result, [])
        mock_print.assert_called_with("Corrupt weather.json, starting fresh.")


class TestSaveWeatherData(unittest.TestCase):
    """Tests for the save_weather_data() function."""

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.makedirs")
    @patch("os.path.dirname", return_value="dummy_path")
    def test_save_data_creates_file(self, mock_dirname, mock_makedirs, mock_file):
        """Should create weather.json file when saving data."""
        data = [{"date": "2025-07-02", "temperature": 25, "humidity": 40, "wind_speed": 10, "precipitation": 0}]
        save_weather_data(data)
        mock_file.assert_called_once_with('beginner/weather_data_analysis/data/weather.json', 'w')

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.makedirs")
    @patch("os.path.dirname", return_value="dummy_path")
    def test_save_data_content(self, mock_dirname, mock_makedirs, mock_file):
        """Should write the correct JSON content to the file."""
        data = [{"date": "2025-07-02", "temperature": 22, "humidity": 50, "wind_speed": 12, "precipitation": 5}]
        save_weather_data(data)
        handle = mock_file()
        expected = json.dumps(data, indent=4)
        handle.write.assert_any_call(expected)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.makedirs")
    @patch("os.path.dirname", return_value="dummy_path")
    def test_save_to_existing_file(self, mock_dirname, mock_makedirs, mock_file):
        """Should overwrite content in an existing file."""
        new_data = [{"date": "2025-07-02", "temperature": 30, "humidity": 45, "wind_speed": 20, "precipitation": 0}]
        save_weather_data(new_data)
        handle = mock_file()
        handle.write.assert_called()


class TestComputeAverage(unittest.TestCase):
    """Tests for the compute_average() function."""

    def test_average_of_valid_list(self):
        """Should return correct average for a valid list of numbers."""
        self.assertEqual(compute_average([10, 20, 30]), 20)

    def test_average_of_empty_list(self):
        """Should return 0 when input list is empty."""
        self.assertEqual(compute_average([]), 0)

    def test_average_of_single_element(self):
        """Should return the value itself if list contains only one number."""
        self.assertEqual(compute_average([100]), 100)


class TestAnalyzeWeather(unittest.TestCase):
    """Tests for the analyze_weather() function."""

    @patch("builtins.print")
    def test_analysis_output_format(self, mock_print):
        """Should print correct summary for known weather dataset."""
        sample = [
            {"date": "2025-07-02", "temperature": 20, "humidity": 30, "wind_speed": 10, "precipitation": 0},
            {"date": "2025-07-02", "temperature": 30, "humidity": 50, "wind_speed": 20, "precipitation": 2}
        ]
        analyze_weather(sample)
        mock_print.assert_any_call("Weather Data Summary")
        mock_print.assert_any_call("Total Records: 2")
        mock_print.assert_any_call("Rainy Days: 1")

    @patch("builtins.print")
    def test_rainy_day_count(self, mock_print):
        """Should count and print correct number of rainy days."""
        sample = [
            {"date": "2025-07-01", "temperature": 20, "humidity": 30, "wind_speed": 10, "precipitation": 0},
            {"date": "2025-07-02", "temperature": 30, "humidity": 50, "wind_speed": 20, "precipitation": 5}
        ]
        analyze_weather(sample)
        mock_print.assert_any_call("Rainy Days: 1")

    @patch("builtins.print")
    def test_extremes_and_averages(self, mock_print):
        """Should correctly calculate min, max, and average values."""
        sample = [
            {"date": "2025-07-01", "temperature": 10, "humidity": 20, "wind_speed": 5, "precipitation": 0},
            {"date": "2025-07-02", "temperature": 30, "humidity": 60, "wind_speed": 15, "precipitation": 0}
        ]
        analyze_weather(sample)
        mock_print.assert_any_call("Average Temperature: 20.00 °C")
        mock_print.assert_any_call("Max Temperature: 30 °C")
        mock_print.assert_any_call("Min Temperature: 10 °C")


class TestAddNewWeatherEntry(unittest.TestCase):
    """Tests for the add_new_weather_entry() function."""

    @patch("builtins.input", side_effect=["28", "35", "15", "3"])
    @patch("main.load_weather_data", return_value=[])
    @patch("main.save_weather_data")
    @patch("builtins.print")
    def test_valid_inputs_add_data(self, mock_print, mock_save, mock_load, mock_input):
        """Should accept valid inputs and call save_weather_data()."""
        add_new_weather_entry()
        self.assertTrue(mock_save.called)
        mock_print.assert_any_call("New entry added successfully!\n")

    @patch("builtins.input", side_effect=["abc", "35", "15", "3"])
    @patch("builtins.print")
    def test_invalid_input_handled_gracefully(self, mock_print, mock_input):
        """Should print error message and skip save if input is invalid."""
        with self.assertRaises(UnboundLocalError):
            add_new_weather_entry()
        mock_print.assert_any_call("Invalid input! Please enter numeric values.\n")

if __name__ == '__main__':
    unittest.main()