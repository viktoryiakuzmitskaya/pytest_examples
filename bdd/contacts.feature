Scenario: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname>, <address> and <homephone>
  When I add the contact to the list
  Then the new contact list is equal to the old list with added contact

  Examples:
  | firstname | lastname | address | homephone |
  | David | Wilson | Tampa, Florida(FL), 33607, 4031 Maryland Avenue | 727-529-4263 |
  | Lisa | Robinson | New York, New York(NY), 10016, 4304 Turkey Pen Road | 917-283-7652 |


Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact

Scenario: Edit a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with new data
  When I enter new contact data
  Then the new contact list is equal to the old list with modified contact
