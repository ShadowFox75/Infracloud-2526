netmask_prefixes = {
'255.255.255.255' :'/32'
,'255.255.255.254':'/31'
,'255.255.255.252':'/30'
 ,'255.255.255.248':'/29'
 ,'255.255.255.240':'/28'
}

def get_net_prefix(p_subnet_mask):
    try:
        net_prefix = netmask_prefixes[p_subnet_mask]
        return net_prefix
    except:
        return "wrong input: garbage in, garbage out"
result = get_net_prefix('255.255.255.255')
print(result)