import uuid
from fastapi import APIRouter

router = APIRouter()

# update a user (authorized user only)
# /:id
# return status 200, and json object with user update, catch errors

# delete a user (authorized user only)
# /:id
# return status 200, and json object with user deletion, catch errors

# get the details of a user, but admin only
# /find/:id
# return status 200, and json object with user details, catch errors, but not password

# get all users, admin only
# /
# query for all users, limit 5
# return status 200, and json object with all users, catch errors
@router.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

# get user stats, admin only
# span last year, get exact month, and number of users created within a certain date
# return 200, and json with users
