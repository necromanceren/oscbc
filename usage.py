import oscbc
o = oscbc.Create()
o.show_policy()
o.show_stu()
o.show_mediaserver()
o.add_policy(policy_name, policy_type, client, target)
o.add_schedule(schedule_name, shcedule_type, schedule_retention, idate)
o.show_client_setup()
o.show_mediaserver_setup()
o.master_shutdown()
