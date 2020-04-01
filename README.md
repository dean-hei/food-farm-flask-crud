## Routes

| Action | Method | Function Name | Path|
|-----|-----|-----|------|
|index| GET | get\_all\_farms() | /farms|
| show | GET | get\_one\_farm() | /farms/:id |
| create | POST | create_farm() | /farms |
| update | PUT | edit_farm() | /farms/:id |
| delete | DELETE | delete_farm() | /farms/:id |


## Schemas

### Farms (1:M with foods)

| Column | Type | Other |
| ----- | ------ | ----|
| id | Integer | PK |
| Name | String | Unique |
| City | String | 

### Foods

| Column | Type | Other |
| ----- | ------ | ----|
| id | Integer | PK |
| Name | String | Unique
| Nutrients | Integer | 
| Food_Group | String |
| Farm_id | Integer | FK|

### Seasons (M:M with foods)

| Column | Type | Other |
|-------|-------|-------|
|id | Integer | PK |
| Name | String | Unique |

