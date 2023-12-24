from sys import stdin
readline = stdin.readline
k,g,m = map(int,readline().rstrip("\n").split())
g_water = 0
m_water = 0
for _ in range(k):
    if g_water == g:
        g_water = 0
    elif m_water == 0:
        m_water = m
    else:
        if m_water == (g - g_water):
            g_water += m_water
            m_water = 0
             
        elif m_water > (g - g_water):
            m_water -= g - g_water
            g_water  = g
        else:
            
            g_water += m_water
            m_water = 0
    #print(str(g_water) + " " + str(m_water))
print(str(g_water) + " " + str(m_water))