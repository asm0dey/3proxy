# 3proxy

In our hard time everyone needs a bit more security. This role helps you
install fast and powerful 3proxy proxy server

**NB**: If some of your servers use iptables (without ufw/firewalld) — you should put role [iptables\_raw](https://github.com/Nordeus/ansible_iptables_raw) into library folder next to your playbook

## Supported OSes

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>name</th>
<th>version</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan=2><p>CentOS</p></td>
<td><p>6</p></td>
</tr>
<tr class="even">
<td><p>7</p></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan=2><p>Ubuntu</p></td>
<td><p>xenial</p></td>
</tr>
<tr class="even">
<td><p>bionic</p></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan=3><p>Fedora</p></td>
<td><p>26</p></td>
</tr>
<tr class="even">
<td><p>27</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>28</p></td>
<td></td>
</tr>
</tbody>
</table>

## Role Variables

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>name</th>
<th>description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>proxy_users</p></td>
<td><p>array of users whch shold have access to proxy (otherwise anybody can)</p></td>
</tr>
<tr class="even">
<td><p>proxy_socks</p></td>
<td><p>enable socks proxy (true by default)</p></td>
</tr>
<tr class="odd">
<td><p>proxy_socks_port</p></td>
<td><p>socks proxy port (1080 be default)</p></td>
</tr>
<tr class="even">
<td><p>proxy_socks_options</p></td>
<td><p>additional socks proxy options</p></td>
</tr>
<tr class="odd">
<td><p>proxy_http</p></td>
<td><p>enable http proxy (true by default)</p></td>
</tr>
<tr class="even">
<td><p>proxy_http_port</p></td>
<td><p>http proxy port (3128 be default)</p></td>
</tr>
<tr class="odd">
<td><p>proxy_http_options</p></td>
<td><p>additional http proxy options</p></td>
</tr>
<tr class="even">
<td><p>manage_firewall</p></td>
<td><p>If role should try to allow incoming connections to proxy on firewall</p></td>
</tr>
</tbody>
</table>

## Proxy users

Proxy user is an object, which consists of 2 fields:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>name</th>
<th>description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>name</p></td>
<td><p>username</p></td>
</tr>
<tr class="even">
<td><p>hash</p></td>
<td><p>hash of the password</p></td>
</tr>
</tbody>
</table>

Hash can be obtained from command
`openssl passwd -1 'yourcomplexpasswordHere'`

## Example Playbook

```yaml
    - hosts: all
      roles:
        - role: 3proxy
          proxy_users:
            - { name: "asm0dey", hash: "$1$pL3Ho94u$2.wCxrLfacj82UMPJSy/6/" }
            - { name: "asm0dey2", hash: "$1$pL3Ho94u$2.wCxrLfacj82UMPJSy/6/" }
```

## Development

You need to have vagrant, docker, ansible and molecule installed to be able to run tests. Of course you can just implemet what you need without tests, but having tests is always better

## License

MIT
