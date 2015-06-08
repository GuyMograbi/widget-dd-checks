

source /vagrant/dev/env.sh

if [ ! -f /usr/bin/node ];then
    echo "installing node"
    NODEJS_VERSION=0.10.35
    NODEJS_HOME=/opt/nodejs
    sudo mkdir -p $NODEJS_HOME
    sudo chown $USER:$USER $NODEJS_HOME
    curl --fail --silent http://nodejs.org/dist/v${NODEJS_VERSION}/node-v${NODEJS_VERSION}-linux-x64.tar.gz -o /tmp/nodejs.tar.gz
    tar -xzf /tmp/nodejs.tar.gz -C ${NODEJS_HOME} --strip-components=1
    sudo ln -s /opt/nodejs/bin/node /usr/bin/node
    sudo ln -s /opt/nodejs/bin/npm /usr/bin/npm

    sudo npm install -g js-yaml # useful for yaml validation js-yaml -t path/to/file.yaml
else
    echo "node already installed"
fi

if [ ! -f /etc/init.d/datadog-agent ];then
    echo "installing datadog"
    bash -c "$(curl -L https://raw.githubusercontent.com/DataDog/dd-agent/master/packaging/datadog-agent/source/install_agent.sh)"
else
    echo "datadog already installed"
fi

sudo rm -rf /etc/dd-agent/checks.d
sudo ln -Tfs /vagrant/checks.d /etc/dd-agent/checks.d

sudo mv /etc/dd-agent/conf.d /etc/dd-agent/orig.conf.d
sudo ln -Tfs /vagrant/conf.d /etc/dd-agent/conf.d

echo "overriding conf.d from dev folder"
cp -f /vagrant/dev/conf.d/* /vagrant/conf.d/

echo "now you can test scripts by running sudo -u dd-agent dd-agent check my_check"