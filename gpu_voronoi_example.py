from fast_gpu_voronoi       import Instance
from fast_gpu_voronoi.jfa   import JFA_star
from fast_gpu_voronoi.debug import save

I = Instance(alg=JFA_star, x=50, y=50, \
        pts=[[ 7,14], [33,34], [27,10],
             [35,10], [23,42], [34,39]])
I.run()

print(I.M.shape)                 # (50, 50, 1)
save(I.M, I.x, I.y, force=True)  # __1_debug.png