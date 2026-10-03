import redis
import json

client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


def save_price(product_id, price):
    data = {
        "product_id": product_id,
        "recommended_price": price
    }

    client.set(
        f"price:{product_id}",
        json.dumps(data)
    )

    print("Price saved to Redis!")


def get_price(product_id):
    data = client.get(f"price:{product_id}")

    if data:
        return json.loads(data)

    return None


if __name__ == "__main__":
    save_price("P0002", 86.52)

    result = get_price("P0002")

    print("Retrieved from Redis:")
    print(result)