import json
import azure.storage as store
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    result = {
        "storage_path": str(store.__path__)
    }

    return func.HttpResponse(body=json.dumps(result), mimetype="application/json")
