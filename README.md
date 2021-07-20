# parsing_kubeconfig

This repository is to a script that concatenate many kubeconfigs file in one.

## How to use
Execute the script related with the python version which you are using.  


**[NOTE]**: The script will try looking for to files which ends like "*-config" in the path that was asked or you can setting customize prefix.  
And it will concatenate every file found in one. You can pass the source directory where the files are stored and the recipient where the file will be save. Also you can keep the default recipients if as well as wished.  

The script will offer the follow questions when is executing:  

Where are stored the kubeconfig files?[/etc/kubernetes]:  
Where do want to save the kubeconfig file?[~/.kube/config]:   
Do you want to change the default prefix?[*-config]: 

After you choose the path and prefix you can configure the current context if you want.  
Do you want to config a current context?[None]:  


To show the contexts in the file use the command: 'kubectl config get-contexts'  
To change the current context: 'kubectl config use-context <context_name>'  
To change the current namespace: 'kubectl config set-context --current --namespace=<namespace>'  

## Example of stdout of executation

```
    *****************************************************************************************************************
      [NOTE]:The script will try looking for to files which ends like "*-config" in the path that was asked or you 
      can setting customize prefix.
      And it will concatenate every file found in one. You can pass the source directory where the files are stored 
      and the recipient where the file will be save. Also you can keep the default recipients if as well as wished.
    *****************************************************************************************************************
    
Where are stored the kubeconfig files?[/etc/kubernetes]: /home/user/kubectl-files
Where do want to save the kubeconfig file?[~/.kube/config]: 
Do you want to change the default prefix?[*-config]: kubeconfig*
 ~> Context created 'context-1'
 ~> Context created 'context-2'
 ~> Context created 'context-3'
 ~> Context created 'context-4'
 ~> Context created 'context-5'

Do you want to config a current context?[None]: context-5

The file was created in "/home/user/.kube/config"

    ~> To show the contexts in the file use the command: 'kubectl config get-contexts'
    ~> To change the current context: 'kubectl config use-context <context_name>'
    ~> To change the current namespace: 'kubectl config set-context --current --namespace=<namespace>'

```