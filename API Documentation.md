## Endpoints

### Calculate View Endpoint

- **URL:** `/calculate/`
- **Method:** POST
- **Parameters:**
  - `zone`: Integer, represents the zone code.
  - `organization_id`: Integer, represents the organization's ID.
  - `total_distance`: Float, represents the total distance in kilometers.
  - `item_type`: String, represents the type of item.
- **Response:**
  - If successful, returns a JSON object with the calculated value.
  - If unsuccessful due to missing or invalid parameters, returns an appropriate error message.

### Organization List Endpoint

- **URL:** `/organization/list/`
- **Method:** GET
- **Response:** Returns a JSON array of organization objects with their details.

### Organization Create Endpoint

- **URL:** `/organization/create/`
- **Method:** POST
- **Parameters:**
  - `name`: String, represents the name of the organization.
  - `address`: String, represents the address of the organization.
  - ... (other organization fields)
- **Response:**
  - If successful, returns a JSON object with the created organization's details.
  - If unsuccessful due to missing or invalid parameters, returns an appropriate error message.

### Item List Endpoint

- **URL:** `/item/list/`
- **Method:** GET
- **Response:** Returns a JSON array of item objects with their details.

### Item Create Endpoint

- **URL:** `/item/create/`
- **Method:** POST
- **Parameters:**
  - `type`: String, represents the type of the item.
  - `description`: String, represents the description of the item.
  - ... (other item fields)
- **Response:**
  - If successful, returns a JSON object with the created item's details.
  - If unsuccessful due to missing or invalid parameters, returns an appropriate error message.

### Pricing List Endpoint

- **URL:** `/pricing/list/`
- **Method:** GET
- **Response:** Returns a JSON array of pricing objects with their details.

### Pricing Create Endpoint

- **URL:** `/pricing/create/`
- **Method:** POST
- **Parameters:**
  - `item_id`: Integer, represents the ID of the item.
  - `organization_id`: Integer, represents the ID of the organization.
  - `zone`: Integer, represents the zone code.
  - `base_distance_in_km`: Float, represents the base distance in kilometers.
  - `km_price`: Float, represents the price per kilometer.
  - `fix_price`: Float, represents the fixed price.
- **Response:**
  - If successful, returns a JSON object with the created pricing's details.
  - If unsuccessful due to missing or invalid parameters, returns an appropriate error message.
