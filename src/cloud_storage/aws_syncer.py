import os


class S3Sync:

    def sync_folder_to_s3(self,folder,aws_folder_path):
        """
        Method Name :   sync_folder_to_s3
        Description :   This method syncs local folder to s3 bucket

        Output      :   NA
        On Failure  :   Write an exception log and then raise an exception

        Version     :   1.2
        Revisions   :   moved setup to cloud
        """

        command = f"aws s3 sync {folder} s3://{aws_folder_path} "
        os.system(command)

    def sync_folder_from_s3(self,folder,aws_folder_path):
        """
        Method Name :   sync_folder_from_s3
        Description :   This method syncs s3 folder to local folder

        Output      :   NA
        On Failure  :   Write an exception log and then raise an exception

        Version     :   1.2
        Revisions   :   moved setup to cloud
        """

        command = f"aws s3 sync s3://{aws_folder_path} {folder} "
        os.system(command)