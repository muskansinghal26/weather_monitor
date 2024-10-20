# test_weather.py

import unittest
from unittest.mock import patch
from weather_service import kelvin_to_celsius, fetch_weather, process_weather_data
from thresholds import set_alert_thresholds, check_alerts

class TestWeatherService(unittest.TestCase):
    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(kelvin_to_celsius(300), 26.85)
        self.assertAlmostEqual(kelvin_to_celsius(273.15), 0)

    @patch('weather_service.requests.get')
    def test_fetch_weather(self, mock_get):
        mock_get.return_value.json.return_value = {'main': {'temp': 300}, 'weather': [{'main': 'Clear'}]}
        result = fetch_weather('TestCity')
        self.assertEqual(result['main']['temp'], 300)
        self.assertEqual(result['weather'][0]['main'], 'Clear')

class TestThresholds(unittest.TestCase):
    def test_set_alert_thresholds(self):
        data = {'temperature_threshold': '35', 'humidity_threshold': '80'}
        result = set_alert_thresholds(data)
        self.assertEqual(result['temperature_threshold'], 35)
        self.assertEqual(result['humidity_threshold'], 80)

    def test_check_alerts(self):
        weather_data = {'city': 'TestCity', 'temperature': 36, 'condition': 'Sunny'}
        with patch('thresholds.alert_thresholds', {
            'temperature': {'city': 'TestCity', 'threshold': 35, 'duration': 1},
            'condition': {'city': 'TestCity', 'condition': 'Rain'}
        }):
            alerts = check_alerts(weather_data)
            self.assertEqual(len(alerts), 1)
            self.assertIn('Temperature alert', alerts[0])

if __name__ == '__main__':
    unittest.main()
