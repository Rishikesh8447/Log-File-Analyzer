from datetime import datetime


# Sample log data


logs = [
    {
        "timestamp": "2026-10-08 10:15:00",
        "log_level": "INFO",
        "message": "User logged in",
        "user_id": 101
    },
    {
        "timestamp": "2026-10-08 10:20:00",
        "log_level": "ERROR",
        "message": "Database connection failed",
        "user_id": 102
    },
    {
        "timestamp": "2026-10-08 10:25:00",
        "log_level": "INFO",
        "message": "Page opened",
        "user_id": 101
    },
    {
        "timestamp": "2026-10-08 11:05:00",
        "log_level": "ERROR",
        "message": "Database connection failed",
        "user_id": 103
    },
    {
        "timestamp": "2026-10-08 11:30:00",
        "log_level": "WARNING",
        "message": "Slow response detected",
        "user_id": 101
    },
    {
        "timestamp": "2026-10-08 11:45:00",
        "log_level": "ERROR",
        "message": "Payment failed",
        "user_id": 104
    },
    {
        "timestamp": "2026-10-08 12:10:00",
        "log_level": "ERROR",
        "message": "Authentication failed",
        "user_id": 105
    },
    {
        "timestamp": "2026-10-08 12:30:00",
        "log_level": "ERROR",
        "message": "Payment failed",
        "user_id": 104
    },
    {
        "timestamp": "2026-10-08 13:15:00",
        "log_level": "INFO",
        "message": "User logged out",
        "user_id": 101
    },
    {
        "timestamp": "2026-10-08 14:20:00",
        "log_level": "ERROR",
        "message": "Server timeout",
        "user_id": 106
    }
]


# 1. Filter ERROR logs

def filter_error_logs(logs):
    error_logs = [
        log
        for log in logs
        if log["log_level"] == "ERROR"
    ]

    return error_logs


# 2. Count log levels

def count_log_levels(logs):
    log_counts = {}

    for log in logs:
        level = log["log_level"]

        if level not in log_counts:
            log_counts[level] = 0

        log_counts[level] += 1

    return log_counts


# 3. Count users

def count_users(logs):
    user_counts = {}

    for log in logs:
        user_id = log["user_id"]

        if user_id not in user_counts:
            user_counts[user_id] = 0

        user_counts[user_id] += 1

    return user_counts


# 4. Find most active user

def find_most_active_user(user_counts):
    most_active_user = None
    highest_count = 0

    for user_id, count in user_counts.items():

        if count > highest_count:
            highest_count = count
            most_active_user = user_id

    return most_active_user


# 5. Group errors by hour

def group_errors_by_hour(error_logs):
    errors_by_hour = {}

    for log in error_logs:

        time = datetime.strptime(
            log["timestamp"],
            "%Y-%m-%d %H:%M:%S"
        )

        hour = time.hour

        if hour not in errors_by_hour:
            errors_by_hour[hour] = 0

        errors_by_hour[hour] += 1

    return errors_by_hour


# 6. Calculate error rate

def calculate_error_rate(logs, error_logs):
    total_logs = len(logs)
    total_errors = len(error_logs)

    if total_logs == 0:
        return 0

    return (total_errors / total_logs) * 100


# 7. Count error messages

def count_error_messages(error_logs):
    error_message_counts = {}

    for log in error_logs:
        message = log["message"]

        if message not in error_message_counts:
            error_message_counts[message] = 0

        error_message_counts[message] += 1

    return error_message_counts


# 8. Find top 5 common errors

def find_top_errors(error_message_counts):
    sorted_errors = sorted(
        error_message_counts.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_errors[:5]


# 9. Find hour with most errors

def find_peak_error_hour(errors_by_hour):
    most_error_hour = None
    highest_error_count = 0

    for hour, count in errors_by_hour.items():

        if count > highest_error_count:
            highest_error_count = count
            most_error_hour = hour

    return most_error_hour, highest_error_count


# 10. Generate final report

def generate_report(
    logs,
    log_counts,
    most_active_user,
    error_rate,
    top_5_errors,
    most_error_hour,
    highest_error_count
):
    print()
    print("========================================")
    print("          LOG ANALYSIS REPORT")
    print("========================================")

    print(f"Total logs processed: {len(logs)}")
    print(f"Error rate: {error_rate:.2f}%")

    print()
    print("Log levels:")

    for level, count in log_counts.items():
        print(f"{level}: {count}")

    print()
    print(f"Most active user: {most_active_user}")

    print()
    print("Top 5 common errors:")

    for message, count in top_5_errors:
        print(f"{message} → {count}")

    print()

    if most_error_hour is not None:
        print(
            f"Time period with most errors: "
            f"{most_error_hour}:00 - {most_error_hour}:59"
        )
        print(f"Number of errors: {highest_error_count}")
    else:
        print("No errors found.")

    print("========================================")


# Main program

def main():

    # Filter errors
    error_logs = filter_error_logs(logs)

    # Count log levels
    log_counts = count_log_levels(logs)

    # Count users
    user_counts = count_users(logs)

    # Find most active user
    most_active_user = find_most_active_user(user_counts)

    # Group errors by hour
    errors_by_hour = group_errors_by_hour(error_logs)

    # Calculate error rate
    error_rate = calculate_error_rate(
        logs,
        error_logs
    )

    # Count error messages
    error_message_counts = count_error_messages(
        error_logs
    )

    # Find top 5 errors
    top_5_errors = find_top_errors(
        error_message_counts
    )

    # Find peak error hour
    most_error_hour, highest_error_count = (
        find_peak_error_hour(errors_by_hour)
    )

    # Nested dictionary
    summary = {
        "log_counts": log_counts,
        "user_counts": user_counts,
        "errors_by_hour": errors_by_hour,
        "error_rate": error_rate
    }

    # Generate final report
    generate_report(
        logs,
        log_counts,
        most_active_user,
        error_rate,
        top_5_errors,
        most_error_hour,
        highest_error_count
    )


if __name__ == "__main__":
    main()