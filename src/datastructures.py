
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
                        {
                            "id": 3443,
                            "name": "Tommy",
                            "age": 5,
                            "lucky_numbers": [1]
                        },
                        {
                            "id": self._generateId(),
                            "name": "John",
                            "age": 33,
                            "lucky_numbers": [7, 13, 22]
                        },
                        {
                            "id": self._generateId(),
                            "name": "Jane",
                            "age": 35,
                            "lucky_numbers": [10, 14, 3]
                        },
                    
                        
                        
                        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        new_member = {
            "id": self._generateId(),
            "name": member.get("name"),
            "age": member.get("age"),
            "lucky_numbers": member.get("lucky_numbers"),
        }
        self._members.append(new_member)
        pass

    def delete_member(self, id):
        # self._members = [member for member in self._members if member["id"] != id]
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
        pass


    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return {
                "id": member["id"],
                "name": member.get("name"),
                "age": member["age"],
                "lucky_numbers": member["lucky_numbers"]
                }
        print(f"Member with ID {id} not found")
        return {"error": "Miembro no encontrado"}
        


    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        # active_members = [member for member in self._members if member.get("active", True)]
        return self._members
   