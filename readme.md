# Programming challenge for SRE Interview

We have the output to the describe_instance AWS API call for an account in JSON format:

```bash
aws ec2 describe-instances --output json > instances.json
```

Please make a program that generates a tab-separated output to the console (or a file) in the language you prefer. The fields in the output should be, for every instance:

- Instance Id
- Instance Type
- Instance Image Id
- Key Name
- Private IP
- Public IP
- Subnet Id

> Note: Please consider one or more fields might not be present for an specific instance, in that case output "N/A"

## Level 2

In case you have time, please also output the content of the following Tags:

- Name
- CostCenter
- Application
- Contact Name
- Contact Email
- Contact Phone

> Note: Please consider that the contact information is stored in just one tag, separated by ";"
