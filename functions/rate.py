import requests
from datetime import date, timedelta
from config import CBU_URL

def get_cbu_rate(expense_date: date) -> float:
    current_date = expense_date
    for _ in range(7):
        try:
            response = requests.get(
                CBU_URL.format(currency="USD", date=current_date.isoformat()),
                timeout=5
            )
            response.raise_for_status()
            data = response.json()
            if data:
                return float(data[0]["Rate"])
        except (
            requests.RequestException,
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            ) as exc:
            raise RuntimeError(
                    f"Failed to fetch or parse the USD exchange rate for "
                    f"{current_date.isoformat()}: {exc}"
                    ) from exc


        current_date -= timedelta(days=1)

    raise RuntimeError(
        "No USD exchange rate found in the 7 days ending "
        f"{expense_date.isoformat()}."
    )


