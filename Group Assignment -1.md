# Group Assignment -1

## Introduction

The mini world describes various dog competitions as part of Crufts, the greatest dog event organized by the Kennel Club. There are several events as parts of championships for all kinds of dogs in Crufts. 

## Purpose

The purpose of this database is to store data about the various championships and the events that are a part of the Crufts Dog show.

## Users

Organizers, Dog trainers(participants), spectators and Sponsors.

## Applications

- Dogs : Stores the data about dogs registered for the event
- Owner : Stores data about a dog’s owner
- Championship : Stores data about championship organized by the Crufts
- Events : Stores data about the events organized as a part of each championship
- Results : Stores the performance of dog in an event

## Database Requirements

### Entities

1. Owner
   - Name : Name of the owner
     - Char(50)
     - Not NULL
   - Email : Email address of the owner
     - Char(100)
     - Not NULL
     - Unique
   - Contact : Contact number of the owner
     - Integer with 8-11 digits
     - Not NULL
   - Nationality : Nationality of the owner
     - Char(3)
     - Has to be from fixed choices of country codes
     - Not NULL
3. Championship
   - Name : Name of the championship
     - Char(50)
     - Not NULL
     - Unique
   - Entry Opening Date : Date after which the participants can register
     - DateTime
     - Not NULL
   - Entry Closing Date : Date after which participants can no longer register themselves
     - DateTime
     - Not NULL
   - Competition start date : Start Date of Competition
     - DateTime
     - Not NULL
   - Competition End Date : End date of competition
     - DateTime
     - Not NULL
3. Judge
   - Judge_id : Unique Id of the judge
     - Integer
     - Unique
     - Not NULL
   - Name : Name of the Judge
     - Char(50)
     - Not NULL
   - Breed : The breed judged by the judge
     - Char(50)
     - Not NULL
4. Dogs
   - Name : Name of the dog
     - Char(50)
     - Not NULL
   - Breed : Breed of the dog
     - Char(50)
     - Not NULL
   - Weight : Weight of the dog
     - 50 > Integer > 5
     - Not NULL
   - Age : Age of the dog
     - 15 > Integer > 2
     - Not NULL
5. Events
   - Type : Type of Event
     - Char(50)
     - Not NULL
   - Allowed Dog Size : The dog size permitted determined by the rules
     - Char(10)
     - Choices = (SMALL, MEDIUM, LARGE, ANY)
     - Not NULL
   - Prizes : Prize Money allocated to the event
     - Integer
     - Not NULL
6. Accommodation
   - Accommodation_id : Unique Id of the kennel
     - Integer > 0
     - Not NULL
   - Size : Size of the kennel
     - Char(10)
     - Choices = (SMALL,MEDIUM,LARGE)
     - Not NULL
   - Rent : Rent price of the kennel
     - Integer
     - Not NULL
   - Availability : Boolean determining the availability of kennel
     - Boolean
     - Not NULL

### Weak Entities

`Dogs` and `Events` are weak entities

### Relationships

1. Owns
   - The relationship between `Owner` and `Dogs`
   - Degree = (1:`Owner`, M:`Dogs`) [2]
   - Cardinality constraint = 0 [cardinality ratio? ]
2. Results
   - Attributes : 
     - Score
       - Integer
   - Relationship between `Dogs` and `Events` storing the score of a dog in an event
   - Degree = (1:`Dogs`, 1: `Events`)
   - Cardinality constraint = 1
3. Accommodates
   - Attributes :
     - Lease Date
       - DateTime
       - Not NULL
     - Lease End Date
       - DateTime
       - Not NULL
   - Relationship between `Dogs`, `Owner` and `Accommodation`
   - Each accommodation houses dogs from various owner. This relationship stores dates at which the accommodation’s leased by the owner for a particular dog
   - Degree = (1:`Dogs`, 1:`Owner`, 1:`Accommodation`)
   - Cardinality Constraint = 1

## Functional Requirements

### Modifications

- Insert : dogs

- Delete : event

- Update : Championship

### Retrieval

- Selection : retrieve all events in a championship

- Projection query : All dogs of a particular breed

- Aggregate: Number of events won by a dog

- Search : search for an event

- Analysis : Total events won by a dog of particular breed



