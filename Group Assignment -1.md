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
     - Char(50), Not NULL
   - Email : Email address of the owner
     - Char(100), Not NULL, Unique
   - Contact : Contact number of the owner
     - Integer with 8-11 digit, Not NULL
   - Nationality : Nationality of the owner
     - Char(3), Has to be from fixed choices of country codes, Not NULL
   
3. Championship
   - Name : Name of the championship
     - Char(50), Not NULL, Unique
   - Entry Opening Date : Date after which the participants can register
     - DateTime, Not NULL
   - Entry Closing Date : Date after which participants can no longer register themselves
     - DateTime, Not NULL
   - Competition start date : Start Date of Competition
     - DateTime, Not NULL
   - Competition End Date : End date of competition
     - DateTime, Not NULL
   
3. Judge
   - Judge_id : Unique Id of the judge
     - Integer, Unique, Not NULL
   - Name : Name of the Judge
     - Char(50), Not NULL
   - Breed : The breed judged by the judge
     - Char(50), Not NULL
   
4. Dogs
   - Name : Name of the dog
     - Char(50), Not NULL
   - Breed : Breed of the dog
     - Char(50), Not NULL
   - Weight : Weight of the dog
     - 50 > Integer > 5, Not NULL
   - Age : Age of the dog
     - 15 > Integer > 2, Not NULL
   
5. Events
   - Type : Type of Event
     - Char(50), Not NULL
   - Allowed Dog Size : The dog size permitted determined by the rules
     - Char(10), Choices = (SMALL, MEDIUM, LARGE, ANY), Not NULL
   - Prizes : Prize Money allocated to the event
     - Integer, Not NULL
   
6. Result

   - Result_id : Unique ID of the result
     - Integer > 0, Not NULL, Unique

   - Score : Score given to the dog
     - Integer, Not NULL

### Weak Entities

`Dogs` and `Events` are weak entities

### Relationships

1. Owns
   - The relationship between `Owner` and `Dogs`, i.e, `Owner` owns `Dogs`
   - Degree = (1:`Owner`, M:`Dogs`)
   - Cardinality constraint = N
2. Judged by
   - Relationship between `Events` and `Judges` such that an `Event` is judged by a `Judge`
   - Degree = (1:`Events`, 1:`Judges`)
   - Cardinality Constraint = 1
3. Result
   - Relationship between `Dogs` and `Events` and `Results` such that its links the `Result` of a `Dog` in an `Event`
   - Degree = (1:`Dogs`, 1: `Events`, 1: `Results`)
   - Cardinality constraint = 1

### n > 2 Relationship

The relationship `Result` is an example of ternary relationship

## Functional Requirements

### Modifications

- Insert : Events, Dog participants, Owners of the participant dogs, Judges

- Delete : Events, Participants, Judges 
- Update : Championship

### Retrieval

- Selection : Winner of an event, List of all dogs participating

- Projection query : All dogs of a particular breed, List of all participants from a particular country

- Aggregate: Number of events won by a dog, Maximum events won by a dog, Maximum participants from any country.

- Search : Search for an event, 

- Analysis : Total events won by a dog of particular breed, Countries will the most winners in events of 

  particular breed size. 
