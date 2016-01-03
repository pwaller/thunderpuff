#! /usr/bin/env python3

from thunderpuff import Template, Param
from thunderpuff.funcs import join

t = Template("My super awesome template.")

HostedZoneName = Param(str, "Name of hosted zone to use")

ServicesDNS = t.add(
    "AWS::Route53::RecordSet",
    HostedZoneName=join(HostedZoneName, ""),
    Name="blah.pdftables.com", Type="A", TTL=60, ResourceRecords=[ServicesEIP],
)

bar = ""

# t.output(ServicesDNS, "DNS name of services instance")
