import getopt
import sys
import json
from MattermostConnector import send_mattermost_notification

HELP_INFORMATION = "\nPossible options are:" \
                   "\n--- Meetings ---\n" \
                   "-d [--daily] - call for daily\n" \
                   "-p [--planning] - call for planning\n" \
                   "-r [--retro] - call for retro\n" \
                   "-v [--review] - call for sprint review\n" \
                   "\n --- Reminders ---\n" \
                   "[--daily_reminder] - daily reminder\n" \
                   "[--planning_reminder] - planning reminder\n" \
                   "[--retro_reminder] - retro reminder\n" \
                   "[--review_reminder] - review reminder\n" \
                   "[--beta_reminder] - release on BETA remainder\n" \
                   "[--production_reminder] - release on production remainder\n"

hook = "None"
username = "None"
messages = {}


def main():
    global hook
    try:
        opts, args = getopt.getopt(sys.argv[1:], "dprv", ["help",
                                                          "daily",
                                                          "retro",
                                                          "planning",
                                                          "review",
                                                          "daily_reminder",
                                                          "planning_reminder",
                                                          "retro_reminder",
                                                          "review_reminder",
                                                          "beta_reminder",
                                                          "production_reminder"])
    except getopt.GetoptError as err:
        print(HELP_INFORMATION)
        sys.exit(2)
    for o, a in opts:
        if o in ("-d", "--daily"):
            send_mattermost_notification(hook, username, messages["daily"])
        if o in "--daily_reminder":
            send_mattermost_notification(hook, username, messages["daily_reminder"])
        elif o in ("-h", "--help"):
            print(HELP_INFORMATION)
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
        else:
            assert False, "unhandled option"


def set_up():
    global hook
    global username
    global messages
    path = 'config.json'
    with open(path) as file:
        data = json.load(file)
        hook = data["evryplaceChannelHook"]
        username = data["defaultUsername"]
        messages["daily"] : data["messages"]


if __name__ == "__main__":
    set_up()
    main()
