import csv

def load_threat_feed(filename):
    threat_data = {}

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            indicator = row["indicator"].strip()
            threat_data[indicator] = {
                "type": row["type"],
                "threat_level": row["threat_level"],
                "description": row["description"]
            }

    return threat_data


def load_iocs(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip()]


def check_iocs(iocs, threat_data):
    results = []

    for ioc in iocs:
        if ioc in threat_data:
            results.append({
                "indicator": ioc,
                "status": "Known malicious/suspicious",
                "type": threat_data[ioc]["type"],
                "threat_level": threat_data[ioc]["threat_level"],
                "description": threat_data[ioc]["description"]
            })
        else:
            results.append({
                "indicator": ioc,
                "status": "Not found",
                "type": "unknown",
                "threat_level": "low",
                "description": "No match found in local threat feed"
            })

    return results


def save_results(results, filename):
    with open(filename, "w", newline="") as file:
        fieldnames = ["indicator", "status", "type", "threat_level", "description"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(results)


def main():
    threat_data = load_threat_feed("threat_feed.csv")
    iocs = load_iocs("iocs_to_check.txt")

    results = check_iocs(iocs, threat_data)
    save_results(results, "results.csv")

    print("Threat intelligence check completed.")
    print("Results saved to results.csv")

    for result in results:
        print(
            result["indicator"],
            "-",
            result["status"],
            "-",
            result["threat_level"]
        )


if __name__ == "__main__":
    main()
    