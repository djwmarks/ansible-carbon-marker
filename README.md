# Ansible carbon marker module

Write "marker" metrics for one or more names. Useful for correlating events
caused by automated processes with platform behaviour (e.g. release
automation.)

```yaml
---
 - name: Example
   tasks:
     - name: Say Hello
	   carbon_marker:
	     host: carbon.example.com
		 name: ansible.hello
```
