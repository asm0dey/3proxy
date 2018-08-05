3proxy
=========

In our hard time everyone needs a bit more security. This role helps you install fast and powerful 3proxy proxy server

Role Variables
--------------

| name                | description                                                            |
|---------------------|------------------------------------------------------------------------|
| proxy_users         | array of users whch shold have access to proxy (otherwise anybody can) |
| proxy_socks         | enable socks proxy (true by default)                                   |
| proxy_socks_port    | socks proxy port (1080 be default)                                     |
| proxy_socks_options | additional socks proxy options                                         |
| proxy_http          | enable http proxy (true by default)                                    |
| proxy_http_port     | http proxy port (3128 be default)                                      |
| proxy_http_options  | additional http proxy options                                          |

Proxy users
-----------

Proxy user is an object, which consists of 2 fields:

| name | description          |
|------|----------------------|
| name | username             |
| hash | hash of the password |

Hash can be obtained from command `openssl passwd -1 'yourcomplexpasswordHere'`

Example Playbook
----------------

    - hosts: all
      roles:
        - role: 3proxy
          proxy_users:
            - { name: "asm0dey", hash: "$1$pL3Ho94u$2.wCxrLfacj82UMPJSy/6/" }
            - { name: "asm0dey2", hash: "$1$pL3Ho94u$2.wCxrLfacj82UMPJSy/6/" }

License
-------

MIT
