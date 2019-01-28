echo "Create a private key from the environment variable..."
echo "$PRIVATE_KEY" | tr '#' '\n' | tr '_' ' ' > id_rsa
chmod 600 id_rsa

echo "Add the host key for the remote server..."
echo 'dev3.default.opendataservices.uk0.bigv.io ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDVUnT1C1bqxOqSwGIRQGbM0KTFDRzG5XeBDosei7I6GCg/9WcsMQ9rjYnOC5YN1j6FoB04S9JU/lzFCnENVTLKvl1mua5Wd209H01QzEV6OL2tC3KbXAMvWtsQSuwPZ0sIYr3PrRBA1eQz6Kd8OaU7+7GdoAUNXJDtgjodmd8yOfE0JQ1dy9XSY6jVUbJ2up+sfexFSO3DR7WlNA3AEi5KBmjqm9R4fI0dnEN/yBKagrAstvg2ojh1KFdjZAZKRRniA2CjkvyhNpiOIWbaPqPNuUhyK3soyCRLZTxcrXafUQ6bdA3wT6RU0QPOxsJJukKHAjBugIH8Fl5DSWODNB53' >> ~/.ssh/known_hosts

echo "Get LFTP binary if necessary..."
if hash lftp 2>/dev/null; then
    LFTP=lftp
else
    wget "https://raw.githubusercontent.com/OpenDataServices/opendataservices-deploy/master/lftp"
    chmod a+x ./lftp
    LFTP=./lftp
fi

# Make a test SSH connection, as LFTP doesn't output key errors well.
# ssh -i id_rsa ocds-docs@dev3.default.opendataservices.uk0.bigv.io

echo "Copy the built files to the remote server..."
# The arguments to mirror are -R for recursive and -e to delete old files
$LFTP -c "set sftp:connect-program \"ssh -i id_rsa\"; connect sftp://ocds-docs:xxx@dev3.default.opendataservices.uk0.bigv.io; mirror -eR build web/$TRAVIS_BRANCH"

echo "Update the search index..."
curl "www.standard-search.default.opendataservices.uk0.bigv.io/v1/index_ocds?secret=${SEARCH_SECRET}&version=${TRAVIS_BRANCH}"