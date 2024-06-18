from fast_gpu_voronoi       import Instance
from fast_gpu_voronoi.jfa   import JFA
from fast_gpu_voronoi.debug import save


I = Instance(alg=JFA, x=1200, y=1200, \
        pts=[[ 7,14], [33,34], [27,10],
             [35,10], [23,42], [34,39]])
I.run()


print(I.M.shape)                 # (50, 50, 1)
save(I.M, I.x, I.y, force=True)  # __1_debug.png0
