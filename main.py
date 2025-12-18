import call_api
import oci
import json


def write_to_bucket(packet, bucket_name, object_name):
    # make client
    signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
    client = oci.object_storage.ObjectStorageClient(config={}, signer=signer)

    # put data
    resp = client.get_namespace()
    namespace = resp.data  # type: ignore

    content = json.dumps(packet)
    client.put_object(namespace, bucket_name, object_name, content)


if __name__ == "__main__":

    # put data to s3
    weather = call_api.get_weather(station_id="WNG736")
    data = call_api.parse_weather(weather)
    bucket_name = "weather-app"

    time_string = f"{data['year']}:{data['month']}:{data['day']}{data['time']}"
    obj_name = f"{data['station_name']}-{time_string}"
    write_to_bucket(packet=data, bucket_name=bucket_name, object_name=obj_name)

    # log sucess
    print(f"Wrote data from {data['station_name']} at {time_string}.")
