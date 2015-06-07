# widget-dd-checks


This project helps you test datadog scripts.

simply put all required environment variables under `synced_folder/dev/env.sh`. This file should look like:

```
export DD_API_KEY="..."
export ANOTHER_KEY="..."
```


Note that `DD_API_KEY` is required by datadog. otherwise the installation will not work.

## Writing a script

put your scripts under `synced_folder/checks.d` and your configurations under `synced_folder/conf.d`
example hello_world from datadog's documentation is built in to the project

Test your script by running `sudo -u dd-agent dd-agent check hello_world`

make sure to replace `hello_world` with your script name




