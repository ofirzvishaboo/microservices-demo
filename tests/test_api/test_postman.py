import subprocess

def run_e2e():
    # Run the collection with basic authentication already configured in Postman
    result = subprocess.run(
        ["newman", "run", "E2E.postman_collection.json", "--insecure", "--reporters", "cli,json", "--reporter-json-export", "report.json"],
        capture_output=True,
        text=True
    )

    # Output results
    print(result.stdout)
    print(result.stderr)

    # Check status
    if result.returncode == 0:
        print("✅ E2E Flow passed successfully!")
    else:
        print("❌ E2E Flow failed!")

if __name__ == "__main__":
    run_e2e()
