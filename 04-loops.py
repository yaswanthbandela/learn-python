# List is a DataStructure which can hold multiple values
# Array -> Data Structure which can hold multiple values of same datatype
list_of_cloud = ["aws","azure","gcp","digital ocean"]
Cloud = "gcp"

print(list_of_cloud)

# add a new cloud, salesforce

list_of_cloud.append("sales force")
print(list_of_cloud)

#add another, ibm cloud
list_of_cloud.append("ibm cloud")
print(list_of_cloud)

list_of_cloud.insert(1,"heroku")
print(list_of_cloud)

list_of_cloud.insert(0,"test cloud")
print(list_of_cloud)

roomates=["lakshman","yaswanth","ananth","gopal"]

for friend in roomates:
    print("the roommate is ",friend)

for i in range(1,5):
    print("You are wonderful")