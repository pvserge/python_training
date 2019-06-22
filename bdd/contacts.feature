Scenario Outline: Add new contact
  Given a contact list
  Given a new contact with <firstname>, <lastname>, <address>, <homephone>, <mobilephone>, <workphone>, <secondaryphone>, <email1>, <email2>, <email3>
  When I add the contact to the list
  Then the new contact list is equal to the old list with added contact
Examples:
  | firstname  | lastname  | address  | homephone  | mobilephone | workphone  | secondaryphone | email1  | email2  | email3  |
  | firstname1 | lastname1 | address1 | 1111111111 | 2222222221  | 3333333331 | 4444444441     | email11 | email21 | email31 |
  | firstname2 | lastname2 | address2 | 1111111112 | 2222222222  | 3333333332 | 4444444442     | email12 | email22 | email32 |


Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact
  When I delete the contact from the list
  Then the new contact list is equal to the contact list with deleted contact


Scenario Outline: Modify a contact
  Given a non-empty contact list
  Given a new contact with <firstname>, <lastname>, <address>, <homephone>, <mobilephone>, <workphone>, <secondaryphone>, <email1>, <email2>, <email3>
  Given a random contact by index to modify
  When I modify the contact
  Then the new contact list is equal to the contact list with modified contact
Examples:
  | firstname  | lastname  | address  | homephone  | mobilephone | workphone  | secondaryphone | email1  | email2  | email3  |
  | firstnameM | lastnameM | addressM | 1111111111 | 2222222221  | 3333333331 | 4444444441     | email1M | email2M | email3M |
