
# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).
 

## [1.0.3] - 2025-08-13
  
 
### Added
 
### Changed
- Breaking change [Inconsistent URLs](https://github.com/alejovicu/nackademin_testautomatisering_kvalit24/issues/154)
    - API renamed from  `POST /products/{product_id}` to `POST /product/{product_id}`
 
### Fixed
 
- [Duplicated products](https://github.com/alejovicu/nackademin_testautomatisering_kvalit24/issues/87)
  `POST /product/{product_id}` will now fail if a prodcut is trying to be added but there is already an
  existing product with the same name in the system.
- [Signup without username and password](https://github.com/alejovicu/nackademin_testautomatisering_kvalit24/issues/122)
  `POST /signup` will now fail if an user with empty username or password is tried to be registred.
- [Can register the same user multiple times](https://github.com/alejovicu/nackademin_testautomatisering_kvalit24/issues/131)
  `POST /signup` will now fail if a user is tryed to be registred but already exist in the system.


## [0.1.0] - 2025-08-13
 
### Added
- Initial Release
   
### Changed
 
### Fixed
 