# Labs 10-14 Submission - Daniel Bostrom

## Completed Labs

### Lab 09 (Prerequisite)
- Jenkins setup with Docker
- Python virtual environment configured
- pytest-version job working

### Labs 10-11: CI/CD Pipeline
- Integration tests job: 2/4 passing (UserAPI.token attribute missing)
- E2E tests job: Playwright browsers not installed in Jenkins (known issue)
- Git integration working
- Test reports generated (JUnit XML + HTML)
- Screenshots: lab_submissions/lab_10_11/

### Lab 12: Regression Testing
- Fixed integration tests for Docker networking (host.docker.internal)
- Updated test files for test suites.
- E2E tests simplified to placeholders (Page Objects incomplete)

### Labs 13-14: Performance Testing
- Locust installed and configured
- Test plan: labs/13_14_performance/TEST_PLAN.md
- Load test executed: 50 concurrent users, 12 minutes, 19,047 requests
- Results: labs/13_14_performance/RESULTS.md
- Screenshots: lab_submissions/lab_13_14/

## Known Issues
1. UserAPI.token attribute not stored after login (2 integration tests fail)
2. E2E tests need Playwright browsers installed in Jenkins
3. E2E Page Object methods incomplete

## Repository
Branch: lab_10_11_12_daniel_bostrom
All code committed and pushed