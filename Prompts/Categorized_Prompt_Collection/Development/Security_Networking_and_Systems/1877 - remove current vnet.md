I have used netgen vnet to deploy that is managed by internal cental team which is geeting deployed by other team for us and managed by them from diffrenct resource group (pc-managed). It hits a road blocker and now we are going to fall back to our old methos to create our own team managed vnet and subnets and not depend on diffrent team managed vnet.

wanted to remove all (comment out) the dependecy from all the modules and resources. and comment of the networking main file so that it gets removed completly. Only once it gets completly removed we can create new vet in our resourse group.


help me with the code to remove current vnet like as in dettact the vnet from all the resources and modules it is acttached as of now. also comment out the networking code so that i can delete all the networking componets incuding the pricate enpoints.

also list down all the resources which are using the vnet. so that its easier to track
