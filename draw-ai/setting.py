# -*- coding: utf-8 -*-

#@markdown ####**Basic Settings:**
batch_name = 'TimeToDisco' #@param{type: 'string'}
steps = 250 #@param [25,50,100,150,250,500,1000]{type: 'raw', allow-input: true}
width_height = [1280, 768]#@param{type: 'raw'}
clip_guidance_scale = 5000 #@param{type: 'number'}
tv_scale =  0#@param{type: 'number'}
range_scale =   150#@param{type: 'number'}
sat_scale =   0#@param{type: 'number'}
cutn_batches = 4  #@param{type: 'number'}
skip_augs = False#@param{type: 'boolean'}

#@markdown ---

#@markdown ####**Init Settings:**
init_image = None #@param{type: 'string'}
init_scale = 1000 #@param{type: 'integer'}
skip_steps = 10 #@param{type: 'integer'}
#@markdown *Make sure you set skip_steps to ~50% of your steps if you want to use an init image.*

#Get corrected sizes
side_x = (width_height[0]//64)*64;
side_y = (width_height[1]//64)*64;
if side_x != width_height[0] or side_y != width_height[1]:
  print(f'Changing output size to {side_x}x{side_y}. Dimensions must by multiples of 64.')

#Update Model Settings
timestep_respacing = f'ddim{steps}'
diffusion_steps = (1000//steps)*steps if steps < 1000 else steps
model_config.update({
    'timestep_respacing': timestep_respacing,
    'diffusion_steps': diffusion_steps,
})

#Make folder for batch
batchFolder = f'{outDirPath}/{batch_name}'
createPath(batchFolder)