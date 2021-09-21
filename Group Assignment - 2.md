# Group Assignment - 2

## ER Diagram

![Group Assignment-2.drawio](/home/vegi/Downloads/Group Assignment-2.drawio.png)

## Analysis of :om:’s Assignment-1

### Errors in data requirements

- Key attributes of all entity types are missing.
- Participation constraints in every relationship are missing. (We couldn’t judge the intended purpose of the entities due to this)
- Domain of the attributes is not specified for any attribute.
- Missing attributes for entity types and undefined entity types:
  - Sponsors [ Not required in the database ]
  - Accommodation tie ups
  - Organizers
  - Broadcasters
  - Hotels
- Redundancy in Entity type `Participating Teams`:
  - Event_name should have been a relationship to the entity type `Events of Crufts.`
  - Members of team is described as  multi valued attribute to participant IDs but should have been a one-many relationship with participants.
- Redundancy in Entity Type `Events of crufts`
  - Number of participants is derived quantity (Not mentioned)
  - Winner must a be relationship with `Participants`
- Sponsors and Event organizers isn’t database in relationship but sponsors are users of the database for accessing visitor information according to description.
- The above relationship was also described as n>3 relationship being a binary relationship.
- Unnecessary entity `Organizer` in the relationship `Participation`, when `Organizer` is only related to the the entity `Events of Crufts`.
- Organizers aren’t required in the relationship `Accommodation` as per the mini world requirements.

### Errors in functional requirements

- The search requirement

  > Search for the events by their types to get their names and the schedule
  > of the event.

  is an example of projection query rather than a search query.

- The analysis requirement

  > Trade Exhibitors can use the Projection to find the events with >10000
  > Visitors (based on the Advanced Bookings using Table of Visitors ) to
  > decide which event to Target.

  is an example of projection query rather than an analysis query.