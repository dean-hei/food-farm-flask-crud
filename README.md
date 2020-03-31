## Routes

| Action | Method | Function Name | Path|
|-----|-----|-----|------|
|index| GET | get\_all\_foods() | /foods|
| show | GET | get\_one\_food() | /foods/:id |
| create | POST | create_food() | /foods |
| update | PUT | edit_food() | /foods/:id |
| delete | DELETE | delete_food() | /foods/:id |


## Schemas

### Foods

| Column | Type | Other |
| ----- | ------ | ----|
| id | Integer | PK |
| Name | String | Unique
| Nutrients | Integer | 
| Type | String |
| Farm_id | Integer | FK


### Farms (1:M with foods)

| Column | Type | Other |
| ----- | ------ | ----|
| id | Integer | PK |
| Name | String | Unique |
| City | String | 

