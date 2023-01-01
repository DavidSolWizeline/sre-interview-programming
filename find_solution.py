"""One way to solve the challenge
"""

# %% Import needed modules
import json
from pprint import pprint

# %% Load the json file into a variable
with open("instances.json", encoding="UTF8") as input_file:
    input_data = json.load(input_file)

pprint(input_data)

# %% Find the "root" elements in the input data
pprint(input_data, depth=1)

# %% Find the content of a reservation
for reservation in input_data["Reservations"]:
    pprint(reservation, depth=1)
    print("=" * 30)

# %% Finds the content of an instance
for instance in input_data["Reservations"][0]["Instances"]:
    pprint(instance, depth=1)
    print("=" * 30)

# %% Get the data of the first instance
instance_sample_data = input_data["Reservations"][0]["Instances"][0]
pprint(instance_sample_data)

# %% Get the level 1 requested information
instance_id = instance_sample_data["InstanceId"]
instance_type = instance_sample_data["InstanceType"]
instance_imageid = instance_sample_data["ImageId"]
instance_keyname = instance_sample_data["KeyName"]
instance_privateip = instance_sample_data["PrivateIpAddress"]
instance_publicip = instance_sample_data["PublicIpAddress"]
subnetid = instance_sample_data["SubnetId"]

print(
    instance_id,
    instance_type,
    instance_imageid,
    instance_keyname,
    instance_privateip,
    instance_publicip,
    subnetid,
    sep="\t",
)

# %% Define a function that takes an instance dictionary and prints its information
def parse_instance(instance_data: dict[str, str]) -> None:
    """Prints the requested data from an instance

    Args:
        instance_data (dict[str, str]): Dict with the data of the instance
    """
    print(
        instance_data["InstanceId"],
        instance_data["InstanceType"],
        instance_data["ImageId"],
        instance_data["KeyName"],
        instance_data["PrivateIpAddress"],
        instance_data["PublicIpAddress"],
        instance_data["SubnetId"],
        sep="\t",
    )


# %% Prints the data for all the instances
print(
    "Instance Id",
    "Type",
    "Image",
    "KeyName",
    "Private IP",
    "Public IP",
    "Subnet Id",
    sep="\t",
)
for reservation in input_data["Reservations"]:
    for instance in reservation["Instances"]:
        parse_instance(instance)

# %% There is an error, need to fix the function
def parse_instance(instance_data: dict[str, str]) -> None:
    """Prints the requested data from an instance

    Args:
        instance_data (dict[str, str]): Dict with the data of the instance
    """
    print(
        instance_data.get("InstanceId", "N/A"),
        instance_data.get("InstanceType", "N/A"),
        instance_data.get("ImageId", "N/A"),
        instance_data.get("KeyName", "N/A"),
        instance_data.get("PrivateIpAddress", "N/A"),
        instance_data.get("PublicIpAddress", "N/A"),
        instance_data.get("SubnetId", "N/A"),
        sep="\t",
    )


# %% Try again
print(
    "Instance Id",
    "Type",
    "Image",
    "KeyName",
    "Private IP",
    "Public IP",
    "Subnet Id",
    sep="\t",
)
for reservation in input_data["Reservations"]:
    for instance in reservation["Instances"]:
        parse_instance(instance)

# %% Level 2, get also the tags values, first get the Tags dictionary
tags = instance_sample_data["Tags"]
pprint(tags)

# %% Get the distinct tag data
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
    tag_name,
    tag_costcenter,
    tag_app,
    tag_contactname,
    tag_contactemail,
    tag_contactphone,
    sep="\t",
)

# %% Add that code to the function
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


# %% Full solution
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
# %%
