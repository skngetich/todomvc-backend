# Todo Sample App Backend
## About the app
A rococo-based backend for web apps

A user can do the following:

Person
- [x] Create user account
- [x] Update user profile infomation
- [x] Update forgotten password via password reset link 
  
Auth
- [x] Login 
- [x] Logout
  
Task
- [x] Create A task
- [x] List Available task
- [x] Update A task
- [x] Delete A task
- [x] Filter A task

## How to Run The App

The application packaged in docker and will run using docker compose.
```sh
./run.sh
```
Alternatively

```sh
docker compose --profile dev up -d
```

Note on windows:
Convert all your `.sh` files from `CRLF` (Windows) to `LF` (Linux) end of line sequence (character) and then save your files after conversion