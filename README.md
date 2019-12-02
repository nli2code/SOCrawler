# SOCrawler
Crawler to download Stack Overflow posts based on Scratch.

## usage
Give permission for `run.sh` (e.g. `chmod 777 run.sh`) and execute the script.

##setting

Settings should be modified in the file`so/setting.py`, the main concern is about the limit for visiting times for certain website.

The following is the current setting, each visit is delayed by one second.

```python
######## the delay is 1 second ############
DOWNLOAD_DELAY = 1.0 
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 1
```

