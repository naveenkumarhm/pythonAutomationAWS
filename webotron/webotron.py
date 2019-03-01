import boto3
import click
session = boto3.Session(profile_name = 'pythonAutomation')
ec2 = session.resource('ec2')

@click.command()
for i in ec2.instances.all():
    print(i.id)
    print(i)
