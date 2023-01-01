"""Program to solve the challenge
"""

# %% Import needed modules
import json

# %% Load the json file into a variable
with open("instances.json", encoding="UTF8") as input_file:
    input_data = json.load(input_file)

# Function to Parse an instance data
def parse_instance(instance_data: dict[str, str]) -> None:
    """Prints the requested data from an instance

    Args:
        instance_data (dict[str, str]): Dict with the data of the instance
    """
    tags = instance_data["Tags"]
    tag_name = "N/A"
    tag_costcenter = "N/A"
    tag_app = "N/A"
    tag_contact = "N/A;N/A;N/A"
    tag_contactname = "N/A"
    tag_contactemail = "N/A"
    tag_contactphone = "N/A"
    for tag in tags:
        if tag["Key"] == "Name":
            tag_name = tag["Value"]
        elif tag["Key"] == "CostCenter":
            tag_costcenter = tag["Value"]
        elif tag["Key"] == "Contact":
            tag_contact = tag["Value"]
            tag_contactname, tag_contactemail, tag_contactphone = tag_contact.split(";")
        elif tag["Key"] == "App":
            tag_app = tag["Value"]
    print(
        instance_data.get("InstanceId", "N/A"),
        instance_data.get("InstanceType", "N/A"),
        instance_data.get("ImageId", "N/A"),
        instance_data.get("KeyName", "N/A"),
        instance_data.get("PrivateIpAddress", "N/A"),
        instance_data.get("PublicIpAddress", "N/A"),
        instance_data.get("SubnetId", "N/A"),
        tag_name,
        tag_costcenter,
        tag_app,
        tag_contactname,
        tag_contactemail,
        tag_contactphone,
        sep="\t",
    )


# Full solution
print(
    "Instance Id",
    "Type",
    "Image",
    "KeyName",
    "Private IP",
    "Public IP",
    "Subnet Id",
    "Name",
    "CostCenter",
    "App",
    "Contact Name",
    "Contact Email",
    "Contact Phone",
    sep="\t",
)
for reservation in input_data["Reservations"]:
    for instance in reservation["Instances"]:
        parse_instance(instance)
