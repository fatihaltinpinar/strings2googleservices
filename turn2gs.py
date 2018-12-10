def turn2gs(tagsNvalues):
    x = '''{
   "project_info": {
    "project_number": "%s",
    "firebase_url": "%s",
    "project_id": "%s",
    "storage_bucket": "%s"
    },
     "client": [
    {
      "client_info": {
        "mobilesdk_app_id": "%s",
        "android_client_info": {
          "package_name": " !!!! ENTER PACKAGE NAME HERE OTHERWISE THIS WILL NOT WORK BITCH"
        }
      },
      "oauth_client": [
        {
          "client_id": "%s",
          "client_type": 3
        }
      ],
      "api_key": [
        {
          "current_key": "%s"
        }
      ],
      "services": {
        "analytics_service": {
          "status": 1
        },
        "appinvite_service": {
          "status": 1,
          "other_platform_oauth_client": []
        },
        "ads_service": {
          "status": 2
        }
      }
    }
    ],
    "configuration_version": "1"
}''' % (tagsNvalues['default_web_client_id'],
           tagsNvalues['firebase_database_url'],
           tagsNvalues['project_id'],
           tagsNvalues['google_storage_bucket'],
           tagsNvalues['google_app_id'],
           tagsNvalues['default_web_client_id'],
           tagsNvalues['google_api_key'])
    return x

