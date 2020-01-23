from unittest import TestCase, mock

from lib.readers.facebook_reader import FacebookMarketingReader

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adsinsights import AdsInsights


class FacebookReaderTest(TestCase):
    DATEFORMAT = "%Y-%m-%d"

    def mock_facebook_reader(self, **kwargs):
        for param, value in kwargs.items():
            setattr(self, param, value)

    kwargs = {
        "ad_insights": True,
        "app_id": "",
        "app_secret": "",
        "access_token": "",
        "ad_object_id": "",
        "recurse_level": 0,
        "ad_object_type": "adaccount",
        "desired_fields": ["date_start", "impressions"],
    }

    @mock.patch("lib.readers.facebook_reader.FacebookMarketingReader.run_query_on_fb_account_obj")
    @mock.patch.object(FacebookMarketingReader, "__init__", mock_facebook_reader)
    @mock.patch.object(FacebookMarketingReader, "get_params", lambda *args: None)
    @mock.patch.object(FacebookAdsApi, "init", lambda *args: None)
    def test_read_empty_data(self, mock_query):
        reader = FacebookMarketingReader(**self.kwargs)
        mock_query.return_value = []
        if len(list(reader.read())) > 1:
            assert False, "Data is not empty"

    @mock.patch("lib.readers.facebook_reader.FacebookMarketingReader.run_query_on_fb_account_obj")
    @mock.patch.object(FacebookMarketingReader, "__init__", mock_facebook_reader)
    @mock.patch.object(FacebookMarketingReader, "get_params", lambda *args: None)
    @mock.patch.object(FacebookAdsApi, "init", lambda *args: None)
    def test_read_data(self, mock_query):
        reader = FacebookMarketingReader(**self.kwargs)
        row1, row2 = AdsInsights(), AdsInsights()
        row1.set_data({"date_start": "2019-01-01", "impressions": "1"})
        row2.set_data({"date_start": "2019-01-01", "impressions": "2"})
        mock_query.return_value = [row1, row2]

        expected = [{"date_start": "2019-01-01", "impressions": "1"}, {"date_start": "2019-01-01", "impressions": "2"}]

        for data in reader.read():
            for record, output in zip(data.readlines(), iter(expected)):
                assert record == output

    @mock.patch.object(FacebookMarketingReader, "__init__", mock_facebook_reader)
    def test_format_standard_field(self):
        kwargs = {"desired_fields": ["clicks", "gender", "impressions"]}
        record = {"clicks": "0", "date_start": "2020-01-01", "gender": "unknown", "impressions": "300"}
        expected = {"clicks": "0", "gender": "unknown", "impressions": "300"}
        assert next(FacebookMarketingReader(**kwargs).format_and_yield(record)) == expected

    @mock.patch.object(FacebookMarketingReader, "__init__", mock_facebook_reader)
    def test_format_nested_field(self):
        kwargs = {"desired_fields": ["outbound_clicks"]}
        record = {"outbound_clicks": [{"action_type": "outbound_click", "value": "1"}]}
        expected = {"outbound_clicks": "1"}
        assert next(FacebookMarketingReader(**kwargs).format_and_yield(record)) == expected

    @mock.patch.object(FacebookMarketingReader, "__init__", mock_facebook_reader)
    def test_format_field_not_in_report(self):
        kwargs = {"desired_fields": ["age", "outbound_clicks"]}
        record = {"gender": "unknown"}
        expected = {"age": None, "outbound_clicks": None}
        assert next(FacebookMarketingReader(**kwargs).format_and_yield(record)) == expected