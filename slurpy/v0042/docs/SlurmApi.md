# slurpy.v0042.SlurmApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_job**](SlurmApi.md#delete_job) | **DELETE** /slurm/v0.0.42/job/{job_id} | cancel or signal job
[**delete_jobs**](SlurmApi.md#delete_jobs) | **DELETE** /slurm/v0.0.42/jobs/ | send signal to list of jobs
[**delete_node**](SlurmApi.md#delete_node) | **DELETE** /slurm/v0.0.42/node/{node_name} | delete node
[**get_diag**](SlurmApi.md#get_diag) | **GET** /slurm/v0.0.42/diag/ | get diagnostics
[**get_job**](SlurmApi.md#get_job) | **GET** /slurm/v0.0.42/job/{job_id} | get job info
[**get_jobs**](SlurmApi.md#get_jobs) | **GET** /slurm/v0.0.42/jobs/ | get list of jobs
[**get_jobs_state**](SlurmApi.md#get_jobs_state) | **GET** /slurm/v0.0.42/jobs/state/ | get list of job states
[**get_licenses**](SlurmApi.md#get_licenses) | **GET** /slurm/v0.0.42/licenses/ | get all Slurm tracked license info
[**get_node**](SlurmApi.md#get_node) | **GET** /slurm/v0.0.42/node/{node_name} | get node info
[**get_nodes**](SlurmApi.md#get_nodes) | **GET** /slurm/v0.0.42/nodes/ | get node(s) info
[**get_partition**](SlurmApi.md#get_partition) | **GET** /slurm/v0.0.42/partition/{partition_name} | get partition info
[**get_partitions**](SlurmApi.md#get_partitions) | **GET** /slurm/v0.0.42/partitions/ | get all partition info
[**get_ping**](SlurmApi.md#get_ping) | **GET** /slurm/v0.0.42/ping/ | ping test
[**get_reconfigure**](SlurmApi.md#get_reconfigure) | **GET** /slurm/v0.0.42/reconfigure/ | request slurmctld reconfigure
[**get_reservation**](SlurmApi.md#get_reservation) | **GET** /slurm/v0.0.42/reservation/{reservation_name} | get reservation info
[**get_reservations**](SlurmApi.md#get_reservations) | **GET** /slurm/v0.0.42/reservations/ | get all reservation info
[**get_shares**](SlurmApi.md#get_shares) | **GET** /slurm/v0.0.42/shares | get fairshare info
[**post_job**](SlurmApi.md#post_job) | **POST** /slurm/v0.0.42/job/{job_id} | update job
[**post_job_allocate**](SlurmApi.md#post_job_allocate) | **POST** /slurm/v0.0.42/job/allocate | submit new job allocation without any steps that must be signaled to stop
[**post_job_submit**](SlurmApi.md#post_job_submit) | **POST** /slurm/v0.0.42/job/submit | submit new job
[**post_node**](SlurmApi.md#post_node) | **POST** /slurm/v0.0.42/node/{node_name} | update node properties
[**post_nodes**](SlurmApi.md#post_nodes) | **POST** /slurm/v0.0.42/nodes/ | batch update node(s)


# **delete_job**
> OpenAPIKillJobResp delete_job(job_id, signal=signal, flags=flags)

cancel or signal job

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0042
from slurpy.v0042.models.open_api_kill_job_resp import OpenAPIKillJobResp
from slurpy.v0042.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0042.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0042.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0042.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0042.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID
    signal = 'signal_example' # str | Signal to send to Job (optional)
    flags = 'flags_example' # str | Signalling flags (optional)

    try:
        # cancel or signal job
        api_response = api_instance.delete_job(job_id, signal=signal, flags=flags)
        print("The response of SlurmApi->delete_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->delete_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 
 **signal** | **str**| Signal to send to Job | [optional] 
 **flags** | **str**| Signalling flags | [optional] 

### Return type

[**OpenAPIKillJobResp**](OpenAPIKillJobResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job signal result |  -  |
**0** | job signal result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_jobs**
> OpenAPIKillJobsResp delete_jobs(kill_jobs_msg=kill_jobs_msg)

send signal to list of jobs

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0042
from slurpy.v0042.models.kill_jobs_msg import KillJobsMsg
from slurpy.v0042.models.open_api_kill_jobs_resp import OpenAPIKillJobsResp
from slurpy.v0042.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0042.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0042.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0042.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0042.SlurmApi(api_client)
    kill_jobs_msg = slurpy.v0042.KillJobsMsg() # KillJobsMsg | Signal or cancel jobs (optional)

    try:
        # send signal to list of jobs
        api_response = api_instance.delete_jobs(kill_jobs_msg=kill_jobs_msg)
        print("The response of SlurmApi->delete_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->delete_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kill_jobs_msg** | [**KillJobsMsg**](KillJobsMsg.md)| Signal or cancel jobs | [optional] 

### Return type

[**OpenAPIKillJobsResp**](OpenAPIKillJobsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | description of jobs to signal |  -  |
**0** | description of jobs to signal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node**
> OpenAPIResp delete_node(node_name)

delete node

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0042
from slurpy.v0042.models.open_api_resp import OpenAPIResp
from slurpy.v0042.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0042.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0042.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0042.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0042.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name

    try:
        # delete node
        api_response = api_instance.delete_node(node_name)
        print("The response of SlurmApi->delete_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->delete_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Node name | 

### Return type

[**OpenAPIResp**](OpenAPIResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node delete request result |  -  |
**0** | node delete request result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diag**
> OpenAPIDiagResp get_diag()

get diagnostics

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0042
from slurpy.v0042.models.open_api_diag_resp import OpenAPIDiagResp
from slurpy.v0042.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0042.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0042.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0042.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0042.SlurmApi(api_client)

    try:
        # get diagnostics
        api_response = api_instance.get_diag()
        print("The response of SlurmApi->get_diag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_diag: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OpenAPIDiagResp**](OpenAPIDiagResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | diagnostic results |  -  |
**0** | diagnostic results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> OpenAPIJobInfoResp get_job(job_id, update_time=update_time, flags=flags)

get job info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0042
from slurpy.v0042.models.open_api_job_info_resp import OpenAPIJobInfoResp
from slurpy.v0042.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0042.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0042.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0042.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0042.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID
    update_time = 'update_time_example' # str | Query jobs updated more recently than this time (UNIX timestamp) (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get job info
        api_response = api_instance.get_job(job_id, update_time=update_time, flags=flags)
        print("The response of SlurmApi->get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 
 **update_time** | **str**| Query jobs updated more recently than this time (UNIX timestamp) | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**OpenAPIJobInfoResp**](OpenAPIJobInfoResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job(s) information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs**
> OpenAPIJobInfoResp get_jobs(update_time=update_time, flags=flags)

get list of jobs

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0042
from slurpy.v0042.models.open_api_job_info_resp import OpenAPIJobInfoResp
from slurpy.v0042.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0042.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0042.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0042.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0042.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Query jobs updated more recently than this time (UNIX timestamp) (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get list of jobs
        api_response = api_instance.get_jobs(update_time=update_time, flags=flags)
        print("The response of SlurmApi->get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Query jobs updated more recently than this time (UNIX timestamp) | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**OpenAPIJobInfoResp**](OpenAPIJobInfoResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job(s) information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs_state**
> OpenAPIJobInfoResp get_jobs_state(job_id=job_id)

get list of job states

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0042
from slurpy.v0042.models.open_api_job_info_resp import OpenAPIJobInfoResp
from slurpy.v0042.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0042.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0042.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0042.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0042.SlurmApi(api_client)
    job_id = 'job_id_example' # str | CSV list of Job IDs to search for (optional)

    try:
        # get list of job states
        api_response = api_instance.get_jobs_state(job_id=job_id)
        print("The response of SlurmApi->get_jobs_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_jobs_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| CSV list of Job IDs to search for | [optional] 

### Return type

[**OpenAPIJobInfoResp**](OpenAPIJobInfoResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) state information |  -  |
**0** | job(s) state information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_licenses**
> OpenAPILicensesResp get_licenses()

get all Slurm tracked license info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0042
from slurpy.v0042.models.open_api_licenses_resp import OpenAPILicensesResp
from slurpy.v0042.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0042.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0042.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0042.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0042.SlurmApi(api_client)

    try:
        # get all Slurm tracked license info
        api_response = api_instance.get_licenses()
        print("The response of SlurmApi->get_licenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_licenses: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OpenAPILicensesResp**](OpenAPILicensesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of get all licenses |  -  |
**0** | results of get all licenses |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node**
> OpenAPINodesResp get_node(node_name, update_time=update_time, flags=flags)

get node info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0042
from slurpy.v0042.models.open_api_nodes_resp import OpenAPINodesResp
from slurpy.v0042.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0042.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0042.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0042.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0042.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name
    update_time = 'update_time_example' # str | Query jobs updated more recently than this time (UNIX timestamp) (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get node info
        api_response = api_instance.get_node(node_name, update_time=update_time, flags=flags)
        print("The response of SlurmApi->get_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Node name | 
 **update_time** | **str**| Query jobs updated more recently than this time (UNIX timestamp) | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**OpenAPINodesResp**](OpenAPINodesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node information |  -  |
**0** | node information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodes**
> OpenAPINodesResp get_nodes(update_time=update_time, flags=flags)

get node(s) info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0042
from slurpy.v0042.models.open_api_nodes_resp import OpenAPINodesResp
from slurpy.v0042.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0042.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0042.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0042.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0042.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Query jobs updated more recently than this time (UNIX timestamp) (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get node(s) info
        api_response = api_instance.get_nodes(update_time=update_time, flags=flags)
        print("The response of SlurmApi->get_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Query jobs updated more recently than this time (UNIX timestamp) | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**OpenAPINodesResp**](OpenAPINodesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node(s) information |  -  |
**0** | node(s) information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_partition**
> OpenAPIPartitionResp get_partition(partition_name, update_time=update_time, flags=flags)

get partition info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0042
from slurpy.v0042.models.open_api_partition_resp import OpenAPIPartitionResp
from slurpy.v0042.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0042.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0042.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0042.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0042.SlurmApi(api_client)
    partition_name = 'partition_name_example' # str | Partition name
    update_time = 'update_time_example' # str | Query partitions updated more recently than this time (UNIX timestamp) (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get partition info
        api_response = api_instance.get_partition(partition_name, update_time=update_time, flags=flags)
        print("The response of SlurmApi->get_partition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_partition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_name** | **str**| Partition name | 
 **update_time** | **str**| Query partitions updated more recently than this time (UNIX timestamp) | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**OpenAPIPartitionResp**](OpenAPIPartitionResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | partition information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_partitions**
> OpenAPIPartitionResp get_partitions(update_time=update_time, flags=flags)

get all partition info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0042
from slurpy.v0042.models.open_api_partition_resp import OpenAPIPartitionResp
from slurpy.v0042.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0042.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0042.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0042.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0042.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Query partitions updated more recently than this time (UNIX timestamp) (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get all partition info
        api_response = api_instance.get_partitions(update_time=update_time, flags=flags)
        print("The response of SlurmApi->get_partitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_partitions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Query partitions updated more recently than this time (UNIX timestamp) | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**OpenAPIPartitionResp**](OpenAPIPartitionResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | partition information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ping**
> OpenAPIPingArrayResp get_ping()

ping test

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0042
from slurpy.v0042.models.open_api_ping_array_resp import OpenAPIPingArrayResp
from slurpy.v0042.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0042.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0042.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0042.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0042.SlurmApi(api_client)

    try:
        # ping test
        api_response = api_instance.get_ping()
        print("The response of SlurmApi->get_ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_ping: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OpenAPIPingArrayResp**](OpenAPIPingArrayResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of ping test |  -  |
**0** | results of ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reconfigure**
> OpenAPIResp get_reconfigure()

request slurmctld reconfigure

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0042
from slurpy.v0042.models.open_api_resp import OpenAPIResp
from slurpy.v0042.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0042.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0042.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0042.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0042.SlurmApi(api_client)

    try:
        # request slurmctld reconfigure
        api_response = api_instance.get_reconfigure()
        print("The response of SlurmApi->get_reconfigure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_reconfigure: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OpenAPIResp**](OpenAPIResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reconfigure request result |  -  |
**0** | reconfigure request result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reservation**
> OpenAPIReservationResp get_reservation(reservation_name, update_time=update_time)

get reservation info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0042
from slurpy.v0042.models.open_api_reservation_resp import OpenAPIReservationResp
from slurpy.v0042.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0042.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0042.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0042.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0042.SlurmApi(api_client)
    reservation_name = 'reservation_name_example' # str | Reservation name
    update_time = 'update_time_example' # str | Query reservations updated more recently than this time (UNIX timestamp) (optional)

    try:
        # get reservation info
        api_response = api_instance.get_reservation(reservation_name, update_time=update_time)
        print("The response of SlurmApi->get_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_reservation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_name** | **str**| Reservation name | 
 **update_time** | **str**| Query reservations updated more recently than this time (UNIX timestamp) | [optional] 

### Return type

[**OpenAPIReservationResp**](OpenAPIReservationResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation information |  -  |
**0** | reservation information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reservations**
> OpenAPIReservationResp get_reservations(update_time=update_time)

get all reservation info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0042
from slurpy.v0042.models.open_api_reservation_resp import OpenAPIReservationResp
from slurpy.v0042.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0042.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0042.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0042.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0042.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Query reservations updated more recently than this time (UNIX timestamp) (optional)

    try:
        # get all reservation info
        api_response = api_instance.get_reservations(update_time=update_time)
        print("The response of SlurmApi->get_reservations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_reservations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Query reservations updated more recently than this time (UNIX timestamp) | [optional] 

### Return type

[**OpenAPIReservationResp**](OpenAPIReservationResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation information |  -  |
**0** | reservation information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shares**
> OpenAPISharesResp get_shares(accounts=accounts, users=users)

get fairshare info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0042
from slurpy.v0042.models.open_api_shares_resp import OpenAPISharesResp
from slurpy.v0042.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0042.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0042.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0042.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0042.SlurmApi(api_client)
    accounts = 'accounts_example' # str | Accounts to query (optional)
    users = 'users_example' # str | Users to query (optional)

    try:
        # get fairshare info
        api_response = api_instance.get_shares(accounts=accounts, users=users)
        print("The response of SlurmApi->get_shares:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->get_shares: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accounts** | **str**| Accounts to query | [optional] 
 **users** | **str**| Users to query | [optional] 

### Return type

[**OpenAPISharesResp**](OpenAPISharesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | shares information |  -  |
**0** | shares information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_job**
> OpenAPIJobPostResponse post_job(job_id, job_desc_msg=job_desc_msg)

update job

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0042
from slurpy.v0042.models.job_desc_msg import JobDescMsg
from slurpy.v0042.models.open_api_job_post_response import OpenAPIJobPostResponse
from slurpy.v0042.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0042.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0042.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0042.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0042.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID
    job_desc_msg = slurpy.v0042.JobDescMsg() # JobDescMsg | Job update description (optional)

    try:
        # update job
        api_response = api_instance.post_job(job_id, job_desc_msg=job_desc_msg)
        print("The response of SlurmApi->post_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->post_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 
 **job_desc_msg** | [**JobDescMsg**](JobDescMsg.md)| Job update description | [optional] 

### Return type

[**OpenAPIJobPostResponse**](OpenAPIJobPostResponse.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job update result |  -  |
**0** | job update result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_job_allocate**
> OpenAPIJobAllocResp post_job_allocate(job_alloc_req=job_alloc_req)

submit new job allocation without any steps that must be signaled to stop

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0042
from slurpy.v0042.models.job_alloc_req import JobAllocReq
from slurpy.v0042.models.open_api_job_alloc_resp import OpenAPIJobAllocResp
from slurpy.v0042.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0042.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0042.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0042.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0042.SlurmApi(api_client)
    job_alloc_req = slurpy.v0042.JobAllocReq() # JobAllocReq | Job allocation description (optional)

    try:
        # submit new job allocation without any steps that must be signaled to stop
        api_response = api_instance.post_job_allocate(job_alloc_req=job_alloc_req)
        print("The response of SlurmApi->post_job_allocate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->post_job_allocate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_alloc_req** | [**JobAllocReq**](JobAllocReq.md)| Job allocation description | [optional] 

### Return type

[**OpenAPIJobAllocResp**](OpenAPIJobAllocResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job allocation response |  -  |
**0** | job allocation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_job_submit**
> OpenAPIJobSubmitResponse post_job_submit(job_submit_req=job_submit_req)

submit new job

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0042
from slurpy.v0042.models.job_submit_req import JobSubmitReq
from slurpy.v0042.models.open_api_job_submit_response import OpenAPIJobSubmitResponse
from slurpy.v0042.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0042.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0042.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0042.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0042.SlurmApi(api_client)
    job_submit_req = slurpy.v0042.JobSubmitReq() # JobSubmitReq | Job description (optional)

    try:
        # submit new job
        api_response = api_instance.post_job_submit(job_submit_req=job_submit_req)
        print("The response of SlurmApi->post_job_submit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->post_job_submit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_submit_req** | [**JobSubmitReq**](JobSubmitReq.md)| Job description | [optional] 

### Return type

[**OpenAPIJobSubmitResponse**](OpenAPIJobSubmitResponse.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job submission response |  -  |
**0** | job submission response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_node**
> OpenAPIResp post_node(node_name, update_node_msg=update_node_msg)

update node properties

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0042
from slurpy.v0042.models.open_api_resp import OpenAPIResp
from slurpy.v0042.models.update_node_msg import UpdateNodeMsg
from slurpy.v0042.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0042.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0042.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0042.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0042.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name
    update_node_msg = slurpy.v0042.UpdateNodeMsg() # UpdateNodeMsg | Node update description (optional)

    try:
        # update node properties
        api_response = api_instance.post_node(node_name, update_node_msg=update_node_msg)
        print("The response of SlurmApi->post_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->post_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Node name | 
 **update_node_msg** | [**UpdateNodeMsg**](UpdateNodeMsg.md)| Node update description | [optional] 

### Return type

[**OpenAPIResp**](OpenAPIResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node update request result |  -  |
**0** | node update request result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_nodes**
> OpenAPIResp post_nodes(update_node_msg=update_node_msg)

batch update node(s)

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurpy.v0042
from slurpy.v0042.models.open_api_resp import OpenAPIResp
from slurpy.v0042.models.update_node_msg import UpdateNodeMsg
from slurpy.v0042.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurpy.v0042.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurpy.v0042.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurpy.v0042.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurpy.v0042.SlurmApi(api_client)
    update_node_msg = slurpy.v0042.UpdateNodeMsg() # UpdateNodeMsg | Nodelist update description (optional)

    try:
        # batch update node(s)
        api_response = api_instance.post_nodes(update_node_msg=update_node_msg)
        print("The response of SlurmApi->post_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->post_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_node_msg** | [**UpdateNodeMsg**](UpdateNodeMsg.md)| Nodelist update description | [optional] 

### Return type

[**OpenAPIResp**](OpenAPIResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | batch node update request result |  -  |
**0** | batch node update request result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

