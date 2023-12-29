"Docker Log UI"

from flask import Flask, request, jsonify, render_template
import docker

app = Flask(__name__)
client = docker.from_env()


@app.route("/get_logs", methods=['GET'])
def get_logs():
    "get logs from a runing container"
    container_id = request.args.get('container_id')
    if not container_id:
        return jsonify({'error': 'Container ID is required'}), 400
    try:
        container_data = client.containers.get(container_id)
        container_name = container_data.name
        logs_bytes = container_data.logs(
            stdout=True,
            stderr=True,
            stream=False,
            timestamps=False,
            tail='all'
        )
        logs_str = logs_bytes.decode('utf-8')
        return render_template('index.html', logs=logs_str, container_id=container_name)
    except docker.errors.NotFound:
        return jsonify({'error': f'Container with ID or NAME {container_id} not found'}), 404
    except docker.errors.APIError as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
