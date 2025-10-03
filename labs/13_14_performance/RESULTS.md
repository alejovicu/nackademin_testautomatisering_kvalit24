# Performance Test Results

## Test Configuration
- Users: 50 concurrent
- Spawn rate: 5 users/second
- Duration: ~12 minutes
- Host: http://localhost:8000

## Results Summary
- Total Requests: 19,047
- Requests/sec: 25 RPS
- Failure Rate: 2.4% (456 failures out of 19,047 requests)
- Average Response Time: 4.82 ms

## Response Times by Endpoint
- **POST /login**: Median 250ms, 95th percentile 280ms, Average 255ms
- **GET /products**: Median 3ms, 95th percentile 7ms, Average 3.29ms
- **POST /signup**: Median 260ms, 95th percentile 510ms, Average 291ms
- **GET /user**: Median 3ms, 95th percentile 7ms, Average 3.36ms
- **POST /user/product/[id]**: Median 3ms, 95th percentile 9ms, Average 4.05ms (456 failures - 19.7% failure rate)

## Analysis
The application performed well overall. Response times for GET endpoints (products, user) were good at 3-7ms for 95th percentile. Login and signup were slower (280-510ms for 95th percentile). The 2.4% overall failure should be further looked into.

## Recommendations
- Investigate the 456 failures on POST /user/product/[id] endpoint - modify test to use valid product IDs only
- Consider implementing better error handling for non-existent product IDs
- Monitor signup/login response times under higher load - approaching upper SLO limits
- Overall system stability is good - sustained 25 RPS with 50 concurrent users