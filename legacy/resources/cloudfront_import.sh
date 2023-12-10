#cloudfront distribution import config

aws cloudfront get-distribution-config \
--id <distribution_id> > distribution_config_backup.json


#Lower the default and max ttl (time to live ) 
#json file from the get-distribution-config api call as you prepare to
#change the distribution.


aws cloudfront update-distribution \
--id <distribution_id> \
--distribution-config file://<new_distribution_config.json>\
--if-match <ETag_value_returned_by_get_config>

# Get the existing Route53 hosted zone and associated
# record sets using the following cli command:


#hosted zone info
aws route53 get-hosted-zone \
--id <hosted_zone_id>

#record set info
aws route53 list-resource-record-sets
--hosted-zone-id <hosted_zone_id>


# Note that the domain servers associated with your NS
# and SOA record sets must match what is listed for the domain
# names you own in Route53 "Registered Domains" listing.

# You can create a new hosted zone for a subdomain
# Ex:
# example.com
# test.example.com

# Each having a distinct hosted zone, just the
# NS and SOA record sets must match
