import docker
import json

client = docker.from_env()

# container_data = client.containers.get("invoice-database")
# container_id = container_data.id
# container_stats = container_data.stats(stream=True, decode=True)
# container_logs = container_data.logs(stdout=True,stderr=True,stream=False,timestamps=False,tail='all')

container_data = client.containers.list()
for c in container_data:
    container_attrs = c.attrs
    print(json.dumps(container_attrs.get('Config').get('Env')))