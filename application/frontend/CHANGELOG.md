
# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).
 

## [1.0.3] - 2025-09-29  

### Added

### Changed

### Fixed
- Fix issue that didn't allow jenkins job to reach the frontend app.
- Fix permission issue to execute the entrypoint script in unix systems.


## [1.0.2] - 2025-09-28
 
### Added
- Required environment variable: VITE_BACKEND_URL
- [Frontend is missing assign/unassign product functionality](https://github.com/alejovicu/nackademin_testautomatisering_kvalit24/issues/160)
  Fix to implement the missing feature that allow users to choose products from the catalog.
 
### Changed
 
### Fixed
- [Login form is not a proper HTML form](https://github.com/alejovicu/nackademin_testautomatisering_kvalit24/issues/135)
  Fix to implement login and signup as HTML forms.
- [User with old token does not get logged out or any prompt that the session has expired](https://github.com/alejovicu/nackademin_testautomatisering_kvalit24/issues/152)
  Now when a token is expired the user would be automatically logged out and redirected to the login page.


## [0.1.0] - 2025-08-13
 
### Added
- Initial Release
   
### Changed
 
### Fixed
 